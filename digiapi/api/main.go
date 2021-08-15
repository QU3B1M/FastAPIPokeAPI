package api

import (
	"digiapi/api/database"
	"log"
)

// API initializes this API
func API() {
	log.Print("Starting app")
	if !database.IsActive() {
		log.Fatal("No DB Connection.")
		return
	}
}
