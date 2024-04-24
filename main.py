from Domain import Domain
from get_config import get_conf
from Headers import Headers


def main() -> None:
    config = get_conf()
    headers = Headers()
    domain = Domain(domain_name=config.domain_name, headers= headers)
    domain.set_headers(config.accept, config.user_agent)
    request = domain.get_request()
    if request:
        domain.set_server_params(request)
        print(f'Сайт {domain.address}')
        print(f'IP хоста {domain.ip}')
        print(domain.check_phone_number(config.phone_pattern))
    else:
        print(f'Сайт {domain.domain_name} не работает')


if __name__ == "__main__":
    main()
