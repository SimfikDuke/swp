from root.db_models import Country
from root.utils import sess

countries_map = [
    (0, 'Any', 'https://image.flaticon.com/icons/svg/197/197591.svg'),
    (1, 'USA', 'https://image.flaticon.com/icons/svg/197/197484.svg'),
    (2, 'Australia', 'https://image.flaticon.com/icons/svg/323/323367.svg'),
    (3, 'S. Africa', 'https://image.flaticon.com/icons/svg/197/197562.svg'),
    (4, 'N. Zealand', 'https://image.flaticon.com/icons/svg/197/197589.svg'),
    (5, 'Italy', 'https://image.flaticon.com/icons/svg/197/197626.svg'),
    (6, 'France', 'https://image.flaticon.com/icons/svg/197/197560.svg'),
    (7, 'Argentina', 'https://image.flaticon.com/icons/svg/197/197573.svg'),
    (8, 'Russia', 'https://image.flaticon.com/icons/svg/197/197408.svg'),
    (9, 'Japan', 'https://image.flaticon.com/icons/svg/197/197604.svg'),
]
if __name__ == '__main__':
    with sess() as session:
        for index, name, flag_url in countries_map:
            exist: Country = session.query(Country).filter(Country.id == index).first()
            if exist is not None:
                exist.name = name
                exist.flag_url = flag_url
            else:
                session.add(Country(name, index, flag_url))
