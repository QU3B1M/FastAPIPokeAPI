package models

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
