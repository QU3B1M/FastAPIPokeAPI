package repository

import (
	"context"
	"digiapi/database"
	"digiapi/database/digifamily"
	"log"
)

// DigiFamily Repository to handle the CRUD.
type DigiFamily struct {
	DB *database.DB
}

// GetAll the family records.
func (fm *DigiFamily) GetAll(ctx context.Context) []digifamily.Model {
	var families []digifamily.Model
	result := fm.DB.Conn.Find(&families)
	if result.Error != nil {
		log.Fatal("Error getting the Digi-Families.")
		return families
	}
	return families
}

// GetOne family record by ID.
func (fm *DigiFamily) GetOne(ctx context.Context, id uint) (digifamily.Model, error) {
	var familyOut digifamily.Model
	result := fm.DB.Conn.Find(&familyOut, id)
	if result.Error != nil {
		log.Fatal("Error getting the Digi-Family.")
		return familyOut, result.Error
	}
	return familyOut, nil
}

// GetByName a family.
func (fm *DigiFamily) GetByName(ctx context.Context, name string) (digifamily.Model, error) {
	var familyOut digifamily.Model
	result := fm.DB.Conn.Where("name = ?", name).Find(&familyOut)
	if result.Error != nil {
		log.Fatal("Error getting the Digi-Family.")
		return familyOut, result.Error
	}
	return familyOut, nil
}

// Create a family record.
func (fm *DigiFamily) Create(ctx context.Context, family *digifamily.Model) error {
	result := fm.DB.Conn.Create(&family)
	if result.Error != nil {
		log.Fatal("Error Creating Digi-Family.")
		return result.Error
	}
	return nil
}

// Update a family record.
func (fm *DigiFamily) Update(ctx context.Context, id uint, family digifamily.Model) error {
	result := fm.DB.Conn.Save(&family)
	if result.Error != nil {
		log.Fatal("Error Updating Digi-Family.")
		return result.Error
	}
	return nil
}

// Delete a family record.
func (fm *DigiFamily) Delete(ctx context.Context, id uint) error {
	result := fm.DB.Conn.Delete(&digifamily.Model{}, id)
	if result.Error != nil {
		log.Fatal("Error Deleting Digi-Family.")
		return result.Error
	}
	return nil
}
