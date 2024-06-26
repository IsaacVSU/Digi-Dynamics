from Connect_DB import connect, close_connection

def create_Table(create_table_query: str):
    connection = connect()
    cursor = connection.cursor()

    print(f"Executing \n{create_table_query}")
    cursor.execute(create_table_query)
    print("SUCCESS in executing!!!!")

    # Finished with Executing queries
    close_connection(cursor=cursor, connection=connection)

# MAY CHANGE Release_Date to DATE type
# Platform may be split between 3 boolean fields
# windows, linux, mac
# Did not include Price overview for demo since it should always be 0.

# Demo NOTE: I didn't make Fullgame_id a foreign key bc it can be null 
#since a game can have a demo and the fullgame hasn't released yet


table_Queries = [
    # Games table
    """
    CREATE TABLE IF NOT EXISTS Games(
    id CHAR(7) PRIMARY KEY, 
    Name VARCHAR(255),
    support_info VARCHAR(255),
    DLC TEXT,
    Base_price INT,
    Current_price INT,
    Developer VARCHAR(255),
    Publisher VARCHAR(255),
    Genre VARCHAR(255),
    Coming_soon Bit(1), 
    Release_Date VARCHAR(255),
    Required_age INT, 
    Controller_Support VARCHAR(255),
    Website VARCHAR(255),
    Short_description TEXT,
    Detailed_description TEXT,
    Supported_languages TEXT,
    windows Bit(1),
    linux Bit(1),
    mac Bit(1),
    Header_image VARCHAR(255)
    );
    """,

    # DLC table

    """
    CREATE TABLE IF NOT EXISTS DLC(
    id CHAR(7) PRIMARY KEY, 
    Name VARCHAR(255),
    support_info VARCHAR(255),
    Base_price INT,
    Current_price INT,
    Developer VARCHAR(255),
    Publisher VARCHAR(255),
    Genre VARCHAR(255),
    Coming_soon Bit(1), 
    Release_Date VARCHAR(255),
    Required_age INT, 
    Controller_Support VARCHAR(255),
    Website VARCHAR(255),
    Short_description TEXT,
    Detailed_description TEXT,
    Supported_languages TEXT,
    windows Bit(1),
    linux Bit(1),
    mac Bit(1),
    Header_image VARCHAR(255),
    Fullgame_id char(7),
    FOREIGN KEY (Fullgame_id) REFERENCES Games(id)
    );
    """,

    # Demo table
    """
    CREATE TABLE IF NOT EXISTS Demo(
    id CHAR(7) PRIMARY KEY, 
    Name VARCHAR(255),
    support_info VARCHAR(255),
    Developer VARCHAR(255),
    Publisher VARCHAR(255),
    Genre VARCHAR(255),
    Release_Date VARCHAR(255),
    Required_age INT, 
    Controller_Support VARCHAR(255),
    Website VARCHAR(255),
    Short_description TEXT,
    Detailed_description TEXT,
    Supported_languages TEXT,
    windows Bit(1),
    linux Bit(1),
    mac Bit(1),
    Header_image VARCHAR(255),
    Fullgame_id char(7)
    );
    """,

    # Movies table
    """
    CREATE TABLE IF NOT EXISTS Movies(
    id CHAR(9) PRIMARY KEY,
    name VARCHAR(255),
    thumbnail VARCHAR(512),
    mp4_480p VARCHAR(512),
    mp4_max VARCHAR(512),
    webm_480p VARCHAR(512),
    webm_max VARCHAR(512),
    game_id char(7),
    FOREIGN KEY (game_id) REFERENCES Games(id)
    );
    """,
    # Music table
    """
    CREATE TABLE IF NOT EXISTS Music(
    id CHAR(7) PRIMARY KEY, 
    Name VARCHAR(255),
    support_info VARCHAR(255),
    Base_price INT,
    Current_price INT,
    Developer VARCHAR(255),
    Publisher VARCHAR(255),
    Coming_soon Bit(1), 
    Release_Date VARCHAR(255),
    Required_age INT, 
    Controller_Support VARCHAR(255),
    Website VARCHAR(255),
    Short_description TEXT,
    Detailed_description TEXT,
    Supported_languages TEXT,
    windows Bit(1),
    linux Bit(1),
    mac Bit(1),
    Header_image VARCHAR(255),
    Fullgame_id char(7),
    FOREIGN KEY (Fullgame_id) REFERENCES Games(id)
    );
    """,
    # user Table
    """
    CREATE TABLE IF NOT EXISTS user(username VARCHAR(255) PRIMARY KEY, pass CHAR(64));
    """,
    
    # LikeGames table
    """
    CREATE TABLE IF NOT EXISTS LikedGames(
        id INT PRIMARY KEY AUTO_INCREMENT, 
        username VARCHAR(255), 
        games_id CHAR(7), 
        FOREIGN KEY (username) REFERENCES user(username), 
        FOREIGN KEY (games_id) REFERENCES Games(id));
    """,

    # LikedDLC table
    """
    CREATE TABLE IF NOT EXISTS LikedDLC(
        id INT PRIMARY KEY AUTO_INCREMENT, 
        username VARCHAR(255), 
        DLC_id CHAR(7), 
        FOREIGN KEY (username) REFERENCES user(username), 
        FOREIGN KEY (DLC_id) REFERENCES DLC(id));
    """
]

for table_query in table_Queries:
    create_Table(table_query)
