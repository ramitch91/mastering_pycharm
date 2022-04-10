import service


def main():
    show_header()
    service.download_info()
    display_results()


def display_results():
    for show_id in range(120, 150):
        info = service.get_episode(show_id)

        print(f'{info.show_id}. {info.title}')


def show_header():
    print('Welcome to the Talk Python info downloader')
    print()


if __name__ == '__main__':
    main()
