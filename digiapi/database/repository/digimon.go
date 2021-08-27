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

// GetAll the digimonIn records.
func (d *Digimon) GetAll(ctx context.Context) []digimon.Model {
	var digimons []digimon.Model
	result := d.DB.Conn.Find(&digimons)
	if result.Error != nil {
		log.Fatal("Error getting the Digimons.")
		return digimons
	}
	return digimons
}

// GetOne digimonIn record by ID.
func (d *Digimon) GetOne(ctx context.Context, id uint) (digimon.Model, error) {
	var digimonOut digimon.Model
	result := d.DB.Conn.Find(&digimonOut, id)
	if result.Error != nil {
		log.Fatal("Error getting the Digimon.")
		return digimonOut, result.Error
	}
	return digimonOut, nil
}

// GetByName a Digimon.
func (d *Digimon) GetByName(ctx context.Context, name string) (digimon.Model, error) {
	var digimonOut digimon.Model
	result := d.DB.Conn.Where("name = ?", name).Find(&digimonOut)
	if result.Error != nil {
		log.Fatal("Error getting the Digimon.")
		return digimonOut, result.Error
	}
	return digimonOut, nil
}

// Create a Digimon record.
func (d *Digimon) Create(ctx context.Context, digimonIn *digimon.Model) error {
	result := d.DB.Conn.Create(&digimonIn)
	if result.Error != nil {
		log.Fatal("Error Creating Digimon.")
		return result.Error
	}
	return nil
}

// Update a Digimon record.
func (d *Digimon) Update(ctx context.Context, id uint, digimonIn digimon.Model) error {
	var digimonDB digimon.Model
	d.DB.Conn.Find(&digimonDB, id)
	result := d.DB.Conn.Model(&digimonDB).Updates(digimonIn)
	if result.Error != nil {
		log.Fatal("Error Updating Digimon.")
		return result.Error
	}
	return nil
}

// Delete a Digimon record.
func (d *Digimon) Delete(ctx context.Context, id uint) error {
	result := d.DB.Conn.Delete(&digimon.Model{}, id)
	if result.Error != nil {
		log.Fatal("Error Deleting Digimon.")
		return result.Error
	}
	return nil
}
