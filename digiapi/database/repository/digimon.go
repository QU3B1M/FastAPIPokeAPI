package repository

import (
	"context"
	"digiapi/database"
	"digiapi/database/digimon"
	"log"
)

// Digimon Repository to handle the CRUD.
type Digimon struct {
	DB *database.DB
}

// GetAll the digimon records.
func (dg *Digimon) GetAll(ctx context.Context) []digimon.Model {
	var families []digimon.Model
	result := dg.DB.Conn.Find(&families)
	if result.Error != nil {
		log.Fatal("Error getting the Digimon.")
		return families
	}
	return families
}

// GetOne digimon record by ID.
func (dg *Digimon) GetOne(ctx context.Context, id uint) (digimon.Model, error) {
	var digimonOut digimon.Model
	result := dg.DB.Conn.Find(&digimonOut, id)
	if result.Error != nil {
		log.Fatal("Error getting the Digimon.")
		return digimonOut, result.Error
	}
	return digimonOut, nil
}

// GetByName a digimon.
func (dg *Digimon) GetByName(ctx context.Context, name string) (digimon.Model, error) {
	var digimonOut digimon.Model
	result := dg.DB.Conn.Where("name = ?", name).Find(&digimonOut)
	if result.Error != nil {
		log.Fatal("Error getting the Digimon.")
		return digimonOut, result.Error
	}
	return digimonOut, nil
}

// Create a digimon record.
func (dg *Digimon) Create(ctx context.Context, digimonIn digimon.Model) error {
	result := dg.DB.Conn.Create(&digimonIn)
	if result.Error != nil {
		log.Fatal("Error Creating Digimon.")
		return result.Error
	}
	return nil
}

// Update a digimon record.
func (dg *Digimon) Update(ctx context.Context, digimonIn digimon.Model) error {
	result := dg.DB.Conn.Save(&digimonIn)
	if result.Error != nil {
		log.Fatal("Error Updating Digimon.")
		return result.Error
	}
	return nil
}

// Delete a digimon record.
func (dg *Digimon) Delete(ctx context.Context, id uint) error {
	result := dg.DB.Conn.Delete(&digimon.Model{}, id)
	if result.Error != nil {
		log.Fatal("Error Deleting Digimon.")
		return result.Error
	}
	return nil
}
