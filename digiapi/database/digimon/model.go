package digimon

import (
	"digiapi/database/digifamily"

	"gorm.io/gorm"
)

// Level or Generation.
type Level string

// Attribute or Specie.
type Attribute string

// Gender is the secondary-sex characteristic.
type Gender string

// Valid levels.
const (
	DigiEgg    Level = "digi_egg"
	Fresh      Level = "fresh"
	InTraining Level = "in_training"
	Rookie     Level = "rookie"
	Champion   Level = "champion"
	Ultimate   Level = "ultimate"
	Mega       Level = "mega"
)

// Valid attributes
const (
	Data     Attribute = "data"
	Vaccine  Attribute = "vaccine"
	Virus    Attribute = "virus"
	Free     Attribute = "free"
	Variable Attribute = "variable"
)

// Valid genders
const (
	Male   Gender = "male"
	Female Gender = "female"
	None   Gender = "none"
)

// Model is a GORM DataBase Model.
type Model struct {
	gorm.Model
	Name            string
	Gender          Gender
	Attribute       Attribute
	DigiEvolutionID *uint  `gorm:"unique"`
	DigiEvolution   *Model `gorm:"foreignkey:ID;association_foreignkey:DigiEvolutionID" json:"-"`
	FamilyID        uint
	Family          digifamily.Model
	Level           Level
	Type            string
}

// Tabler sets the Model tablename.
type Tabler interface {
	TableName() string
}

// TableName overrides the table name used by Digimon to `digimons`
func (Model) TableName() string {
	return "digimons"
}
