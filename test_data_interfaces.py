import sql_interface
import vector_interface

if __name__ == "__main__":
    print(sql_interface.get_recording_path(1))
    print(sql_interface.get_text_as_dict(1))
    print(sql_interface.get_text_as_dict(2))

    vector_interface.reset_database()
    # print(vector_interface.add_vector_from_content(0, 1, "I love bananas"))
    # print(vector_interface.add_vector_from_content(0, 2, "Inception is a mind-bending movie."))
    # print(vector_interface.add_vector_from_content(0, 3, "The Shawshank Redemption has a powerful storyline."))
    # print(vector_interface.add_vector_from_content(0, 4, "Titanic is a classic romantic film."))
    # print(vector_interface.add_vector_from_content(0, 5, "Artificial intelligence is transforming industries."))
    # print(vector_interface.add_vector_from_content(0, 6, "The latest smartphone features advanced facial recognition."))
    # print(vector_interface.add_vector_from_content(0, 7, "Blockchain technology ensures secure transactions."))
    # print(vector_interface.add_vector_from_content(0, 8, "Exploring Machu Picchu is on my bucket list."))
    # print(vector_interface.add_vector_from_content(0, 9, "The beaches of Maldives are breathtaking."))
    # print(vector_interface.add_vector_from_content(0, 10, "Paris is known as the city of love."))
    # print(vector_interface.add_vector_from_content(0, 11, "Soccer is the most popular sport worldwide."))
    # print(vector_interface.add_vector_from_content(0, 12, "Michael Jordan is considered one of the greatest basketball players."))
    # print(vector_interface.add_vector_from_content(0, 13, "The Olympic Games showcase athletic excellence."))
    # print(vector_interface.add_vector_from_content(0, 14, "The theory of relativity revolutionized physics."))
    # print(vector_interface.add_vector_from_content(0, 15, "DNA is the building block of life."))
    # print(vector_interface.add_vector_from_content(0, 16, "The Mars rover is exploring the red planet for signs of life."))
    # print(vector_interface.get_n_closest_ids(0, "space", 3))
    # print(vector_interface.get_n_closest_ids(0, "love", 3))
    # print(vector_interface.get_n_closest_ids(0, "sports", 3))
    # print(vector_interface.get_n_closest_ids(0, "technology", 3))
    vector_interface.peek_database()
    print(vector_interface.get_n_closest_ids(1, "place", 3))
    print(sql_interface.add_recording("example-prof1s.wav"))
    print(sql_interface.add_recording("example-psychs.wav"))
    print(sql_interface.get_unresumed_recordings())
    print(sql_interface.get_untranscribed_recordings())
