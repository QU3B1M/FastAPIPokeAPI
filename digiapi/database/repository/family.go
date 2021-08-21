package repository

import (
	"context"
	"digiapi/database"
	"digiapi/database/family"
	"log"
)

// Family Repository to handle the CRUD.
type Family struct {
	DB *database.DB
}

// GetAll the family records.
func (fm *Family) GetAll(ctx context.Context) []family.Model {
	var families []family.Model

	result := fm.DB.Conn.Find(&families)
	if result.Error != nil {
		log.Fatal("Error getting the families.")
	}
	return families
}
