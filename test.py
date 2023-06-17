import data

data.Data.Table.new_table(
    "twitter",
    '"id"	INTEGER,"username"	TEXT UNIQUE,"email"	TEXT UNIQUE,"password"	TEXT,"epassword"	TEXT,"adate"	INTEGER,"condtion"	TEXT,"price"	INTEGER,"dateadd"	TEXT,PRIMARY KEY("id" AUTOINCREMENT)'
)