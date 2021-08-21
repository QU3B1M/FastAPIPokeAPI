package digimon

import (
	family "digiapi/database/digifamily"

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
	Name          string
	Gender        Gender
	DigiEvolution *Model `gorm:"many2many:digievlolutions"`
	Attribute     Attribute
	Family        family.Model `gorm:"foreignKey:Name"`
	Level         Level
	Type          string
}
