package models

import "gorm.io/gorm"

type Digimon struct {
	gorm.Model
	Name        string
	Digievolution        string
	Gender        	string
	Level        string
	ModeChange        string
	Attribute        string
	Family        string
	Type        string
}
