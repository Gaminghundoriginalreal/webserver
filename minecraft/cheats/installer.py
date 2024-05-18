import time
import webbrowser


def show_progress_and_redirect():
    progress = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    for value in progress:
        print(f"{value}%")
        time.sleep(1)

    # Weiterleitung zur Webseite
    webbrowser.open("https://gaminghund.de/minecraft/cheats/clients.html")


if __name__ == "__main__":
    show_progress_and_redirect()
