'''
The unittest module allows us to override setUp and tearDown methods for these types of things. So we will create a setUp method that will create the database and a tearDown method that will delete it when the test is over. Note that the setup and tear down will occur for each test. This prevents the tests from altering the database in such a way that a subsequent test will fail.
'''
import os
import mysqlite3_db
import sqlite3
import unittest
 
class TestMusicDatabase(unittest.TestCase):
    """
    Test the music database
    """
 
    def setUp(self):
        """
        Setup a temporary database
        """
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()
 
        # create a table
        cursor.execute("""CREATE TABLE albums
                          (title text, artist text, release_date text,
                           publisher text, media_type text)
                       """)
        # insert some data
        cursor.execute("INSERT INTO albums VALUES "
                       "('Glow', 'Andy Hunter', '7/24/2012',"
                       "'Xplore Records', 'MP3')")
 
        # save data to database
        conn.commit()
 
        # insert multiple records using the more secure "?" method
        albums = [('Exodus', 'Andy Hunter', '7/9/2002',
                   'Sparrow Records', 'CD'),
                  ('Until We Have Faces', 'Red', '2/1/2011',
                   'Essential Records', 'CD'),
                  ('The End is Where We Begin', 'Thousand Foot Krutch',
                   '4/17/2012', 'TFKmusic', 'CD'),
                  ('The Good Life', 'Trip Lee', '4/10/2012',
                   'Reach Records', 'CD')]
        cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)",
                           albums)
        conn.commit()
 
    def tearDown(self):
        """
        Delete the database
        """
        os.remove("mydatabase.db")
        
    def test_updating_artist(self):
        """
        Tests that we can successfully update an artist's name
        """
        mysqlite3_db.update_artist('Red', 'Redder')
        actual = mysqlite3_db.select_all_albums('Redder')
        expected = [('Until We Have Faces', 'Redder',
                     '2/1/2011', 'Essential Records', 'CD')]
        self.assertListEqual(expected, actual)
     
    def test_artist_does_not_exist(self):
        """
        Test that an artist does not exist
        """
        result = mysqlite3_db.select_all_albums('Redder')
        self.assertFalse(result)

    '''
    The setUp method will create our database and then populate it with some data. The tearDown method will delete our database file. If you were using something like MySQL or Microsoft SQL Server for your database, then you would probably just drop the table, but with sqlite, we can just delete the whole thing.

    Now let’s add a couple of actual tests to our code. You can just add these to the end of the test class above:

    python -m unittest test_sqlite3_db.py
    '''
        
