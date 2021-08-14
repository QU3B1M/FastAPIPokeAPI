package api

import (
	"log"
	"digiapi/api/database"
)

// API initializes this API
func Api() {
	if !database.IsActive() {
		log.Fatal("No DB Connection.")
		return
	}
}
