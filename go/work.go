package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"os/exec"
	"strings"
)

func messageDay() {
	fmt.Println("Opening the softwares ...")
	fmt.Println("")
}

func openChrome(sites []string) {
	fmt.Println("Opening the Chrome ...")
	for i := 0; i < len(sites); i++ {
		cmd := exec.Command("open", "-a", "/Applications/Google Chrome.app", sites[i])
		err := cmd.Run()

		if err != nil {
			log.Fatalf("cmd.Run() failed with %s\n", err)
		}
	}
}

func openPrograms(programs []string) {
	for i := 0; i < len(programs); i++ {
		fmt.Println("Opening the software:", programs[i])
		cmd := exec.Command("open", "-a", "/Applications/"+programs[i])
		err := cmd.Run()

		if err != nil {
			log.Fatalf("cmd.Run() failed with %s\n", err)
		}
	}
}

func readCommand() string {
	fmt.Print("Enter a command: ")
	reader := bufio.NewReader(os.Stdin)
	input, err := reader.ReadString('\n')

	if err != nil {
		log.Fatal(err)
	}

	input = strings.TrimSpace(input)
	return input
}

func stopPrograms(programs []string) {
	for _, p := range programs {
		program := strings.ReplaceAll(p, " ", "\\ ")
		command := "ps aux |grep " + program + " |awk '{print $2}' |xargs kill -15"

		cmd := exec.Command("bash", "-c", command)
		err := cmd.Run()

		if err != nil {
			log.Fatalf("cmd.Run() failed with %s\n", err)
		}

	}
}
func main() {
	messageDay()
	command := readCommand()

	sites := []string{"www.google.com.br"}
	programs := []string{"Microsoft Outlook.app", "Microsoft Teams.app", "Visual Studio Code.app"}

	switch command {
	case "start":
		openChrome(sites)
		openPrograms(programs)
		os.Exit(0)
	case "stop":
		fmt.Println("Stopping ...")
		stopPrograms(programs)
	default:
		fmt.Println("There was a error")
		os.Exit(-1)
	}

}
