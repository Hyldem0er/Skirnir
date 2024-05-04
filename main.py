from src.ui import MainWindow
import sys
from PyQt5.QtWidgets import QApplication
from src.utils.stylecss import GlobalStyleSheet
import argparse
from loguru import logger
import datetime
from src.utils.start_research import start_profile_research

# For scripts
config = {
    "handlers": [
        {"sink": sys.stdout, "format": "<green>{time}</green> <level>{message}</level>"},
        {"sink": "file.log", "serialize": True},
    ],
}
logger.configure(**config)

def main():
    parser = argparse.ArgumentParser(prog="Skirnir",
                                     description="")
    
    # Add a --log argument to specify the log level (default is INFO)
    parser.add_argument("--firstname", "-f", action='store', default="", type=str, help="The firstname")
    parser.add_argument("--lastname", "-l", action='store', default="", type=str, help="The lastname")
    parser.add_argument("--birthday", "-b", action='store', default="", type=str, help='Format DD-MM-YYYY')
    parser.add_argument("--alias", "-al", action='store', default="", type=str, help="The alias")
    parser.add_argument("--instagram", "-ig", action='store_true', help="Enable crawl on Instagram")
    parser.add_argument("--facebook", "-fb", action='store_true', help="Enable crawl on Facebook")
    parser.add_argument("--x", "-x", action='store_true', help="Enable crawl on X (Twitter)")
    parser.add_argument("--linkedin", "-lin", action='store_true', help="Enable crawl on LinkedIn")
    parser.add_argument("--tiktok", "-t", action='store_true', help="Enable crawl on TikTok")
    parser.add_argument("--all", "-a", action='store_true', help="Enable crawl on all social networks (enabled by default)")
    parser.add_argument("--deepcrawl", "-", action='store_true', help="Enable deepcrawl")
    parser.add_argument("--pseudo_size", "-ps", nargs=2, type=int, default=(9, 9), metavar=('start', 'end'), help="The range of sizes for generating possible pseudonyms (deepcrawl)")
    parser.add_argument("--alias_only", "-no", action='store_true', help="Make a crawl only for aliases")
    parser.add_argument("--keyword", "-k", action='store', default="", type=str, help="Add this keyword or a query to a crawl")
    parser.add_argument("--export_nickname", "-csv", action='store_true', help="Export the generated nicknames in CSV")
    parser.add_argument("--proxyfile", action="store", default="", type=str, help="Filepath for custom public/private proxy list import")
    parser.add_argument("--log", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], default="CRITICAL", help="Set the log level with the given choices")
    parser.add_argument("--ui", action="store_true", help="Launch the UI mode")


    args = parser.parse_args()


    # Update the logger configuration based on the log level specified
    
    logger.remove()  # Remove the default logger configuration
    logger.add(sys.stdout, format="<green>{time}</green> <level>{message}</level>", level=args.log)
    logger.add("file.log", serialize=True, level="DEBUG")  # Log DEBUG and above to the log file

    logger.info("Enter the program")

    if args.ui:
        app = QApplication(sys.argv)
        # Apply the above Stylesheet to the application
        app.setStyleSheet(GlobalStyleSheet)
        window = MainWindow.MainWindow()
        window.show()
        sys.exit(app.exec())
    else:
        if args.all:
            args.instagram = True
            args.facebook = True
            args.x = True
            args.linkedin = True
            args.tiktok = True
        crawl_list, advanced_profile_set, social_networks_dict = start_profile_research(args.instagram, args.facebook, args.x, args.linkedin,args.tiktok,
                                                                                        args.firstname, args.lastname, args.birthday, args.alias, 
                                                                                        args.birthday != "", args.alias_only, args.pseudo_size,
                                                                                        args.deepcrawl, args.export_nickname, args.keyword, args.proxyfile)
        if args.deepcrawl:
            print(advanced_profile_set)
        else:
            print(crawl_list)


# main method
if __name__ == '__main__':
    main()