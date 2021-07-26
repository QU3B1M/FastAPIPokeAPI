from typing import List

from .base import BaseRepository
from api.database.schemas import Pokemon, PokeType, PokeMove
from api.models import PokemonIn, PokemonOut, PokemonUpdate


class PokemonRepository(BaseRepository[Pokemon, PokemonIn, PokemonOut]):
    """Repository that handles the Pokemon CRUD"""

    model: Pokemon = Pokemon
    pydantic: PokemonOut = PokemonOut

    @classmethod
    async def create(cls, obj_in: PokemonIn) -> PokemonOut:
        """Creates a Pokemon and Assingns its types."""
        # Creates the Pokemon.
        pokemon: Pokemon = await cls.model.create(
            name=obj_in.name, description=obj_in.description
        )
        # Adds the PokeTypes and PokeMoves.
        await cls.add(pokemon, obj_in.types_ids, obj_in.moves_ids)

        return await cls.pydantic.from_tortoise_orm(pokemon)

    @classmethod
    async def update(cls, obj_in: PokemonUpdate, **kwargs) -> bool:
        pokemon: Pokemon = cls.model.get(**kwargs)
        # Add and/or Delete the objects to the relation.
        await cls.add(pokemon, obj_in.types_to_add, obj_in.moves_to_add)
        await cls.remove(pokemon, obj_in.types_to_remove, obj_in.moves_to_remove)

        if not isinstance(obj_in, dict):
            # Converts the object to a dict.
            update_data: dict = obj_in.dict(exclude_unset=True)

        return await pokemon.update(**update_data)

    @classmethod
    async def add(
        cls, pokemon: Pokemon, types_ids: List[int], moves_ids: List[int]
    ) -> None:
        """Adds an object (PokeType or PokeMove) to the relation."""
        # Get the objects to add.
        types: List[PokeType] = [await PokeType.get(id=id) for id in types_ids]
        moves: List[PokeMove] = [await PokeMove.get(id=id) for id in moves_ids]
        # Add the objects to the relation.
        [await pokemon.types.add(type) for type in types]
        [await pokemon.moves.add(move) for move in moves]

    @classmethod
    async def remove(
        cls, pokemon: Pokemon, types_ids: List[int], moves_ids: List[int]
    ) -> None:
        """Removes an object (PokeType or PokeMove) from the relation."""
        # Get the objects to remove.
        types: List[PokeType] = [await PokeType.get(id=id) for id in types_ids]
        moves: List[PokeMove] = [await PokeMove.get(id=id) for id in moves_ids]
        # Remove the objects from the relation.
        [await pokemon.types.remove(type) for type in types]
        [await pokemon.moves.remove(move) for move in moves]
