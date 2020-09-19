package main

import (
	"flag"
	"fmt"
	"github.com/go-telegram-bot-api/telegram-bot-api"
	"github.com/mqu/go-notify"
	"os"
	"strconv"
)

func localNotify(title, body string) {
	notify.Init("Notification")
	notification := notify.NotificationNew(title, body, "")
	if notification == nil {
		fmt.Fprintf(os.Stderr, "Unable to create new notification\n")
	}
	notify.NotificationShow(notification)
	notify.UnInit()
}

func remoteNotify(title, body string) {
	chatID, _ := strconv.Atoi(os.Getenv("BARKY_TG_CHAT"))
	token := os.Getenv("BARKY_TG_TOKEN")
	bot, err := tgbotapi.NewBotAPI(token)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error: %s", err)
	}

	message := fmt.Sprintf("%s\n\n%s", title, body)

	msg := tgbotapi.NewMessage(int64(chatID), message)
	bot.Send(msg)
}

func init() {
	flag.Usage = func() {
		h := "Easy to use and setup notification utility. Supports local and remote (Telegram) notification.\n\n"

		h += "Usage:\n"
		h += "  barky [OPTIONS] [[TITLE] [BODY]|[BODY]]\n\n"

		h += "Options:\n"
		h += "  -l, --local   Local notification\n"
		h += "  -r, --remote  Remote notification\n"
		h += "\n"

		h += "Environment variables:\n"
		h += "  BARKY_TG_TOKEN  Telegram Bot's token\n"
		h += "  BARKY_TG_CHAT   Telegram Chat ID (need to be started)\n"
		h += "\n"

		h += "Setup:\n"
		h += "  export BARKY_TG_TOKEN=xxxxxx\n"
		h += "  export BARKY_TG_CHAT=xxxxxx\n"
		h += "\n"

		fmt.Fprintf(os.Stderr, h)
	}
}

func main() {
	var (
		localFlag  bool
		remoteFlag bool
	)

	flag.BoolVar(&localFlag, "local", false, "")
	flag.BoolVar(&localFlag, "l", false, "")
	flag.BoolVar(&remoteFlag, "remote", false, "")
	flag.BoolVar(&remoteFlag, "r", false, "")

	flag.Parse()

	var title, body string

	if len(flag.Args()) >= 2 {
		title, body = flag.Arg(0), flag.Arg(1)
	} else if len(flag.Args()) == 1 {
		title, body = "barky", flag.Arg(0)
	} else {
		title, body = "barky", "PING"
	}

	if localFlag {
		localNotify(title, body)
	}
	if remoteFlag {
		remoteNotify(title, body)
	}

	if !localFlag && !remoteFlag {
		localNotify(title, body)
		remoteNotify(title, body)
	}
}
