import random
random.seed(0)

db = []

names = ['Agape', 'Aggie', 'Amore', 'Audi', 'Cheska', 'Chia', 'Cyan', 'Elowen', 'Esty', 'Gitty', 'Harbor', 'Harpa', 'Heavenleigh', 'Hennessy', 'Holiday', 'Hyacinth', 'Juju', 'Kapri', 'Kutty', 'Lark', 'Lynix', 'Mahogany', 'Melrose', 'Merci', 'Monet', 'Moon', 'Neo', 'Nisan', 'Nivea', 'Nixon', 'Pixie', 'Portia', 'Posey', 'Quorra', 'Rhythm', 'Royce', 'Saffron', 'Salima', 'Sea', 'Seneca', 'Sephora', 'Sparrow', 'Stormie', 'Tempest', 'Tymber', 'Violina', 'Yolo', 'Zani', 'Zeek', 'Zuly', 'Albin', 'Anthem', 'Basil', 'Bender', 'Berk', 'Blayde', 'Braven', 'Castle', 'Charleston', 'Dagon', 'Darko', 'Denim', 'Dior', 'Dodge', 'Elvin', 'Ember', 'Eron', 'Falcon', 'Finnick', 'Guru', 'Hershey', 'Hilton', 'Indy', 'Jhase', 'Judge', 'Keats', 'Koy', 'Lorde', 'Matix', 'Mclean', 'Moody', 'Nashton', 'Onix', 'Patch', 'Piers', 'Ranger', 'Rexx', 'Rocko', 'Roper', 'Senne', 'Simba', 'Tallon', 'Taro', 'Tiger', 'Viggo', 'Vino', 'Walden', 'Wolf', 'Zealand', 'Zeppelin', 'Emma', 'Liam', 'Mason', 'Jacob', 'William', 'Ethan', 'Michael', 'Alexander', 'James', 'Daniel', 'Olivia', 'Sophia', 'Isabella', 'Ava', 'Mia', 'Emily', 'Abigail', 'Madison', 'Charlotte']

for n in names:
	db.append([n, random.randint(0, 105), 0, []])