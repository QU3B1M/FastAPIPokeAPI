package models

import (
	"gorm.io/gorm"
)

// Digimon is a GORM DataBase Model.
type Digimon struct {
	gorm.Model
	Name          string
	Gender        Gender
	Digievolution *Digimon `gorm:"many2many:digievlolutions"`
	Attribute     Attribute
	Family        Family `gorm:"foreignKey:Name"`
	Level         Level
	Type          string
}
