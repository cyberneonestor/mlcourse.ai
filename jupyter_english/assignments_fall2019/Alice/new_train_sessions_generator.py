from tqdm import tqdm
import csv
import pickle


path = r'D:/Programming/DS/mlcourse/course/jupyter_english/assignments_fall2019/Alice/train/other_user_logs/'
num_sites = 8

def session_file_maker(FILES_PATH, NUM_SITES):

    pkl = r'D:/Programming/DS/mlcourse/course/jupyter_english/assignments_fall2019/Alice/site_dic.pkl'
    sites_dict = {}
    with open(pkl, 'rb') as f:
        sites_dict = pickle.load(f)

    all_users_data = []
    session_index = 1

    fieldnames = 'session_id' + ','
    for i in range(1, NUM_SITES + 1):
        fieldnames += 'site' + str(i) + ',' + 'time' + str(i) + ','
    fieldnames += 'target'

    all_users_data.append(fieldnames)

    for i in tqdm(range(1, 4000)):
        user_data = []
        file_path = FILES_PATH + 'user' + str(10000 + i)[1:] + '.csv'
        try:
            with open(file_path, 'r') as f:
                csv_file = csv.reader(f)
                for row in csv_file:
                    user_data.append(row)
        except FileNotFoundError:
            continue
        user_data.pop(0)

        for k in range(len(user_data) // NUM_SITES):
            session = str(session_index) + ','
            session_data = user_data[k * NUM_SITES : k * NUM_SITES + NUM_SITES]
            for timestemp, site in session_data:
                session += str(sites_dict[site]) + ',' + timestemp + ','
            session += str(0)
            session_index += 1
            all_users_data.append(session)
        
        """
        last_data_in_file = len(user_data) % NUM_SITES
        if last_data_in_file > 0:
            session = str(session_index) + ','
            session_data = user_data[-last_data_in_file:]
            for timestemp, site in session_data:
                session += str(sites_dict[site]) + ',' + timestemp + ','
            session += ',' * (NUM_SITES - last_data_in_file)
            session += str(0)
            session_index += 1
            all_users_data.append(session)
        """

    alice_data = []
    path_alice = r'D:/Programming/DS/mlcourse/course/jupyter_english/assignments_fall2019/Alice/train/Alice_log.csv'

    with open(path_alice, 'r') as f:
            csv_file = csv.reader(f)
            for row in csv_file:
                alice_data.append(row)
    alice_data.pop(0)

    for k in range(len(alice_data) // NUM_SITES):
        session = str(session_index) + ','
        session_data = alice_data[k * NUM_SITES : k * NUM_SITES + NUM_SITES]
        for timestemp, site in session_data:
            session += str(sites_dict[site]) + ',' + timestemp + ','
        session += str(1)
        session_index += 1
        all_users_data.append(session)
        """
        last_data_in_file = len(alice_data) % NUM_SITES
        if last_data_in_file > 0:
            session = str(session_index) + ','
            session_data = alice_data[-last_data_in_file:]
            for timestemp, site in session_data:
                session += str(sites_dict[site]) + ',' + timestemp + ','
            session += ',' * (NUM_SITES - last_data_in_file)
            session += str(1)
            session_index += 1
            all_users_data.append(session)
        """
    output_file_path = FILES_PATH + 'train_sessions_' + str(NUM_SITES) + '_files.csv'

    with open(output_file_path, "w", newline='') as out_file:

        writer = csv.writer(out_file)
        for line in all_users_data:
            writer.writerow(line.split(','))

    

session_file_maker(FILES_PATH=path, NUM_SITES=num_sites)