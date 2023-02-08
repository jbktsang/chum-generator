from datetime import datetime
from replit import db
import random

# TODO: load in peeps from chummers.txt?
peeps = [
  'Cam',
  'Chloe',
  'Jess',
  'Jemima',
  'Natalie',
  'Andre',
  'Max',
  # 'Ellie',
  'Sarah',
  'Fish',
  'Ryan',
  'Aravinth',
  'Lauren',
  'Shihan',
  'Alison'
]


def print_db():
  for key in db.keys():
    print(f"{key}: {list(db[key])}")


def add_pairs_to_db(pairs):
  for pair in pairs:
    db[pair[0]].append(pair[1])
    db[pair[1]].append(pair[0])

    if len(pair) == 3:
      db[pair[0]].append(pair[2])
      db[pair[2]].append(pair[0])
      db[pair[1]].append(pair[2])
      db[pair[2]].append(pair[1])


def format_pairs(pairs):
  formatted_string = f"""
                         .
                        ":"
                      ___:____     |"\/"|
                    ,'        `.    \  /
          .         |  O        \___/  |
^~^~\_____)\_____^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~ 
    /--v____ __°<     CHUM TIME
            )/           
            '
"""
  
  for pair in pairs:
    formatted_string += f"{pair[0]}, {pair[1]}\n"
  return formatted_string


def gen_pairs():
  pairs = []
  third_wheel = None

  while True:
    peeps_copy = list(peeps)

    potential_pairs = []
    while len(peeps_copy) > 1:
      choices = random.sample(peeps_copy, k=2)
      potential_pairs.append(choices)

      peeps_copy.remove(choices[1])
      peeps_copy.remove(choices[0])

    if len(peeps_copy) == 1:
      third_wheel = peeps_copy.pop()

    is_clean_pair = True
    for pair in potential_pairs:
      if pair[1] in db[pair[0]]:
        is_clean_pair = False

    if is_clean_pair:
      pairs = potential_pairs
      break

  if third_wheel:
    pairs[0].append(third_wheel)

  return pairs


def export_db():
  # hi jess
  with open(f"db_saves/{datetime.now()}.txt", "a") as f:
    for key in db.keys():
      string_builder = f"{key}:"
      for val in db[key]:
        string_builder += f"{val} "
      f.write(f"{string_builder.strip()}\n")

    f.close()


def load_db():
  # clear db
  db.clear()
  with open("db_saves/2023-02-08 18:45:34.787931.txt") as f:
    # Strips newline char
    line = f.readline()[:-1]
    while line:
      key = line.split(':')[0]
      db[key] = []
      vals = line.split(':')[1].split(' ')
      for val in vals:
        db[key].append(val)

      # Strips newline char
      line = f.readline()[:-1]


def main():
  rerun_generation = True
  while rerun_generation:
    pairs = gen_pairs()
    print(format_pairs(pairs))

    print("Do these pairs look good? (yes/no)")
    answer = input()
    if answer == "yes":
      print(
        "Finalizing pairs. Adding chums to database and exporting save file.")

      print("CURRENTLY DOES NOTHING.... remove this when below is uncommented.")
      # add_pairs_to_db(pairs)
      # export_db()
      rerun_generation = False
    elif answer == "no":
      print("The database has not been updated, do not use the pairs above.")
      print("Rerun generation? (yes/no)")
      rerun_generation = True if input() == "yes" else False
    else:
      print("Invalid answer, goodbye.")
      rerun_generation = False


main()