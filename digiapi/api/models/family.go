package models

import "gorm.io/gorm"

// Family is a GORM DataBase Model.
type Family struct {
	gorm.Model
	Name         string
	Abbreviation string
	Description  string
	Emblem       string
}
