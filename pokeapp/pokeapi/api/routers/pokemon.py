from fastapi import APIRouter

from ..database.repositories.pokemon import PokemonRepository
from ..models.pokemon import PokemonIn, PokemonOut

router = APIRouter(prefix="/pokemon", tags=["Pokemons"])


@router.get("/")
async def get_all_pokemons():
    """
    ## Retrieves a Pokemon List.

    Path Parameters
    ---------------
        None

    Body Parameters
    ---------------
        None

    Returns
    -------
        List[Pokemon]
    """


@router.get("/{id}")
async def get_pokemon(id: int):
    """
    ## Retrieves a Pokemon List.

    Path Parameters
    ---------------
        id: int                 Pokemon ID.

    Body Parameters
    ---------------
        None

    Returns
    -------

        id: int                 Pokemon ID.
        name: str               Name of the Pokemon.
        description: str        Description of the Pokemon
        gender: PokeGenders     Gender of the Pokemon (M/F)
        types: List[PokeType]   Type/s of the Pokemon
        moves: List[PokeMove]   Move/s of the Pokemon

    """


@router.post("/create", response_model=PokemonOut)
async def create_pokemon(poke_in: PokemonIn):
    """
    ## Retrieves a Pokemon List.

    Path Parameters
    ---------------
        id: int                 Pokemon ID.

    Body Parameters
    ---------------
        None

    Returns
    -------

        id: int                 Pokemon ID.
        name: str               Name of the Pokemon.
        description: str        Description of the Pokemon
        gender: PokeGenders     Gender of the Pokemon (M/F)
        types: List[PokeType]   Type/s of the Pokemon
        moves: List[PokeMove]   Move/s of the Pokemon

    """
    return await PokemonRepository.create(poke_in)
