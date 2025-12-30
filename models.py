from database import get_connection
import random
import sqlite3

valid_categories=["top","bottom","shoes"]
valid_seasons=["summer","winter","fall","all"]
valid_occasion=["casual","party","formal"]
Neutrals=["black","white","grey","gray","beige","brown","navy","denim"]
Warm=["red","orange","yellow","pink"]
Cool=["blue","green","purple"]

def color_group(color):
    c=color.strip().lower()
    if c in Neutrals:
        return "NEUTRALS"
    if c in Warm:
        return "WARM"
    if c in Cool:
        return "COOL"
    return "OTHER"
def get_item_by_id(item_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM items WHERE id=?", (item_id,))
    result = cur.fetchone()
    conn.close()
    return result
def get_all_items():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM items")
    items = cur.fetchall()
    conn.close()
    return items

def compatible_color(c1,c2):
    g1=color_group(c1)
    g2=color_group(c2)
    if g1=="NEUTRALS" or g2=="NEUTRALS":
        return True
    if g1==g2 and g1!="OTHER":
        return True
    if g1=="OTHER" or g2=="OTHER":
        return True
    return False

def add_items(name, category,color,season,occasion,image_path=None):
    con=get_connection()
    try:
        cursor=con.cursor()

        cursor.execute("""INSERT INTO items(name,category,color,season,occasion,image_path) 
                   values(?,?,?,?,?,?)""",(name,category,color,season,occasion,image_path))
        con.commit()
        con.close()
        return True
    except sqlite3.IntegrityError as e:
        return False
    


def list_items():
    con=get_connection()
    cursor=con.cursor()
    query="SELECT * FROM items"
    cursor.execute(query)
    records=cursor.fetchall()
    con.close()
    return records

def delete_items(id):
    con=get_connection()
    cursor=con.cursor()
    cursor.execute("""DELETE FROM items
                   WHERE id=?""",
                   (id,))
    con.commit()
    con.close()

def update_item(id,name,category,color,season,occasion,image_path=None):
    con=get_connection()
    cursor=con.cursor()

    cursor.execute("""UPDATE items
                    SET name=?, category=?,color=?,season=?,occasion=?,image_path=?
                   WHERE id=?""",
                    (name,category,color,season,occasion,image_path,id))
    con.commit()
    con.close()

def search_name(name):
    con=get_connection()
    cursor=con.cursor()
    cursor.execute("SELECT * FROM items WHERE lower(name) LIKE ?",
                   ('%'+name.lower()+'%',))
    records=cursor.fetchall()
    con.close()
    return records
    
def suggest_outfit(season="all",occasion="casual"):
    con=get_connection()
    cursor=con.cursor()
    cursor.execute("""SELECT * FROM items
                   WHERE category='top' AND (season=? OR season='all') 
                   AND (occasion=? OR occasion='casual')""",(season,occasion))
    tops=cursor.fetchall()
    cursor.execute("""SELECT * FROM items
                   WHERE category='bottom' AND (season=? OR season='all') 
                   AND (occasion=? OR occasion='casual')""",(season,occasion))
    bottoms=cursor.fetchall()
    cursor.execute("""SELECT * FROM items
                   WHERE category='shoes' AND (season=? OR season='all') 
                   AND (occasion=? OR occasion='casual')""",(season,occasion))
    shoes=cursor.fetchall()
    con.close()
    print(f"\n----------SUGGESTEF OUTFIT FOR {season}/{occasion}----------\n")
    if not tops:
        print("YOU HAVE NO SUITABLE TOP FOR THIS OUTFIT!")
        return
    if not bottoms:
        print("YOU HAVE NO SUITABLE BOTTOM FOR THIS OUTFIT!")
        return
    valid_pairs=[]
    for t in tops:
        for b in bottoms:
            if compatible_color(t[3],b[3]):
                valid_pairs.append(t,b)
    if valid_pairs:
        top_item,bottom_item=random.choice(valid_pairs)

    else:
        print("NO PERFECT COLOR MATCH")
        top_item=random.choice(tops)
        bottom_item=random.choice(bottoms)
    shoes_choice=None
    if shoes:
        match_top=[s for s in shoes if compatible_color(s[3],top_item[3])]
        if match_top:
            shoes_choice=random.choice(match_top)
        else:
            match_bottom=[s for s in shoes if compatible_color(s[3],bottom_item[3])]
            if match_bottom:
                shoes_choice=random.choice(match_bottom)
            else:
                shoes_choice=random.choice(shoes)
    print(f"-TOP: {top_item[1]} ({top_item[3]})\n")
    print(f"-BOTTOM: {bottom_item[1]} ({bottom_item[3]})\n")
    if shoes_choice:
        print(f"-SHOES: {shoes_choice[1]} ({shoes_choice[3]})\n")
    else:
        print("-SHOES: None")


   

def random_outfit(season,occasion):
    con=get_connection()
    cursor=con.cursor()
    cursor.execute("""SELECT * FROM items
                   WHERE category='top' AND (season=? OR season='all') 
                   AND (occasion=? OR occasion='casual')""",(season,occasion))
    tops=cursor.fetchall()
    cursor.execute("""SELECT * FROM items
                   WHERE category='bottom' AND (season=? OR season='all') 
                   AND (occasion=? OR occasion='casual')""",(season,occasion))
    bottoms=cursor.fetchall()
    cursor.execute("""SELECT * FROM items
                   WHERE category='shoes' AND (season=? OR season='all') 
                   AND (occasion=? OR occasion='casual')""",(season,occasion))
    shoes=cursor.fetchall()
    con.close()
    print(f"\n----------RANDOM OUTFIT FOR {season}/{occasion}----------\n")
    if not tops:
        print("YOU HAVE NO SUITABLE TOP FOR THIS OUTFIT!")
        return
    if not bottoms:
        print("YOU HAVE NO SUITABLE BOTTOM FOR THIS OUTFIT!")
        return
    top=random.choice(tops)
    bottom=random.choice(bottoms)
    shoe=random.choice(shoes) if shoes else "None"

    print(f"-TOP: {top[1]} ({top[3]})\n")
    print(f"-BOTTOM: {bottom[1]} ({bottom[3]})\n")
    if shoe:
        print(f"-SHOES: {shoe[1]} ({shoe[3]})\n")