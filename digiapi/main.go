package main

import (
	"digiapi/api"
	"digiapi/database"
	"log"
	"os"
	"os/signal"
)

func main() {
	database.Connect()

	serv, err := api.New()
	if err != nil {
		log.Fatal(err)
	}

	// start the server.
	go serv.Start()

	// Wait for an in interrupt.
	c := make(chan os.Signal, 1)
	signal.Notify(c, os.Interrupt)
	<-c

	// Attempt a graceful shutdown.
	serv.Close()
}
