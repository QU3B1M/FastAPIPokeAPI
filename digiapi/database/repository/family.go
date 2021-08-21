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
		log.Fatal("Error getting the Digi-Families.")
		return families
	}
	return families
}

// GetOne family record by ID.
func (fm *Family) GetOne(ctx context.Context, id uint) (family.Model, error) {
	var familyOut family.Model
	result := fm.DB.Conn.Find(&familyOut, id)
	if result.Error != nil {
		log.Fatal("Error getting the Digi-Family.")
		return familyOut, result.Error
	}
	return familyOut, nil
}

// GetByName a family.
func (fm *Family) GetByName(ctx context.Context, name string) (family.Model, error) {
	var familyOut family.Model
	result := fm.DB.Conn.Where("name = ?", name).Find(&familyOut)
	if result.Error != nil {
		log.Fatal("Error getting the Digi-Family.")
		return familyOut, result.Error
	}
	return familyOut, nil
}

// Create a family record.
func (fm *Family) Create(ctx context.Context, familyIn family.Model) error {
	result := fm.DB.Conn.Create(&familyIn)
	if result.Error != nil {
		log.Fatal("Error Creating Digi-Family.")
		return result.Error
	}
	return nil
}

// Update a family record.
func (fm *Family) Update(ctx context.Context, familyIn family.Model) error {
	result := fm.DB.Conn.Save(&familyIn)
	if result.Error != nil {
		log.Fatal("Error Updating Digi-Family.")
		return result.Error
	}
	return nil
}

// Delete a family record.
func (fm *Family) Delete(ctx context.Context, id uint) error {
	result := fm.DB.Conn.Delete(&family.Model{}, id)
	if result.Error != nil {
		log.Fatal("Error Deleting Digi-Family.")
		return result.Error
	}
	return nil
}
