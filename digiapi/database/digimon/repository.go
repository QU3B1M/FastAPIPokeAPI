package digimon

import (
	"context"
)

// Repository handle the CRUD operations with Digimons.
type Repository interface {
	GetAll(ctx context.Context) ([]Model, error)
	GetOne(ctx context.Context, id uint) (Model, error)
	GetByName(ctx context.Context, name string) (Model, error)
	Create(ctx context.Context, user *Model) error
	Update(ctx context.Context, id uint, user Model) error
	Delete(ctx context.Context, id uint) error
}
