# What each file contains

There are three folder each containing one of the following : 
 - **Names** that contain only ascii characters:
   - *Александр* would be *Alexander*
 - **Names** that contain UTF-8 characters

- **Words** that are entirely written with UTF-8 characters 

Everything is in the following json format
> language_nameOrWord.json 
>
Each file will look something like this
```py
["Lotte", "Meike", "Romy", "Sepp", "Imke", "Ilse", .... ]
```

All files are **totally valid json** and they've been compressed to save space


# Detailed Length
Here is a detailed Overview in JSON format of the length of each file generated using the generator.py script

```py
{'All_Languages_words.json': 99000, 'afrikaans_names_asci.json': 731, 'american_names_asci.json': 32, 'Anglo-Saxon_names_asci.json': 345, 'Arabic_names_asci.json': 982, 'Armenian_names_asci.json': 70, 'Cambodian_names_asci.json': 15, 'Catalan_names_asci.json': 42, 'Celtic_names_asci.json': 667, 'Chinese_names_asci.json': 85, 'Danish_names_asci.json': 115, 'Dutch_names_asci.json': 1000, 'Egyptian_names_asci.json': 39, 'English_names_asci.json': 1000, 'Finnish_names_asci.json': 226, 'French_names_asci.json': 1000, 'Georgian_names_asci.json': 26, 'German_names_asci.json': 1000, 'Greek_names_asci.json': 1000, 'Haiwaian_names_asci.json': 158, 'Hebrew_names_asci.json': 28, 'Hindi_names_asci.json': 936, 'Hungarian_names_asci.json': 268, 'Icelandic_names_asci.json': 33, 'Iranian_names_asci.json': 40, 'Irish_names_asci.json': 1000, 'Italian_names_asci.json': 694, 'japanese_names_asci.json': 359, 'Jewish_names_asci.json': 83, 'Latin_names_asci.json': 1000, 'Lithuanian_names_asci.json': 33, 'Maori_names_asci.json': 17, 'Norwegian_names_asci.json': 126, 'Persian_names_asci.json': 84, 'Polish_names_asci.json': 220, 'Portugese_names_asci.json': 231, 'Roman_names_asci.json': 90, 'Russian_names_asci.json': 284, 'Scandinavian_names_asci.json': 193, 'Scotish_names_asci.json': 626, 'Slavic_names_asci.json': 282, 'Spanish_names_asci.json': 885, 'Thai_names_asci.json': 23, 'Turkish_names_asci.json': 133, 'Vietnamese_names_asci.json': 95, 'Welsh_names_asci.json': 931, 'finished_language_file.json': 6, 'package.json': 10, 'testingnet.json': 6, 'trained-net.json': 6, 'Full_names_ascii.json': 17500, 'arabian_names.json': 473, 'english_names.json': 1992, 'greek_names.json': 437, 'Albanian_words.json': 1000, 'Arabic_words.json': 1000, 'Armenian_words.json': 1000, 'Azerbaijani_words.json': 1000, 'Basque_words.json': 1000, 'Belarusian_words.json': 1000, 'Bengali_words.json': 1000, 'Bosnian_words.json': 1000, 'Bulgarian_words.json': 1000, 'Catalan_words.json': 1000, 'Cebuano_words.json': 1000, 'Chichewa_words.json': 1000, 'Chinese_words.json': 1000, 'Corsican_words.json': 1000, 'Croatian_words.json': 1000, 'Czech_words.json': 1000, 'Danish_words.json': 1000, 'Dutch_words.json': 1000, 'English_words.json': 1000, 'Esperanto_words.json': 1000, 'Estonian_words.json': 1000, 'Filipino_words.json': 1000, 'Finnish_words.json': 1000, 'French_words.json': 1000, 'Frisian_words.json': 1000, 'Galician_words.json': 1000, 'Georgian_words.json': 1000, 'German_words.json': 1000, 'Greek_words.json': 1000, 'Gujarati_words.json': 1000, 'Haitian_words.json': 1000, 'Hausa_words.json': 1000, 'Hawaiian_words.json': 1000, 'Hebrew_words.json': 1000, 'Hindi_words.json': 1000, 'Hmong_words.json': 1000, 'Hungarian_words.json': 1000, 'Icelandic_words.json': 1000, 'Igbo_words.json': 1000, 'Indonesian_words.json': 1000, 'Irish_words.json': 1000, 'Italian_words.json': 1000, 'Japanese_words.json': 1000, 'Javanese_words.json': 1000, 'Kannada_words.json': 1000, 'Kazakh_words.json': 1000, 'Khmer_words.json': 1000, 'Korean_words.json': 1000, 'Kurdish_words.json': 1000, 'Kyrgyz_words.json': 1000, 'Lao_words.json': 1000, 'Latin_words.json': 1000, 'Latvian_words.json': 1000, 'Lithuanian_words.json': 1000, 'Luxembourgish_words.json': 1000, 'Macedonian_words.json': 1000, 'Malagasy_words.json': 1000, 'Malayalam_words.json': 1000, 'Malaysian_words.json': 1000, 'Maltese_words.json': 1000, 'Maori_words.json': 1000, 'Marathi_words.json': 1000, 'Mongolian_words.json': 1000, 'Myanmar_words.json': 1000, 'Nepali_words.json': 1000, 'Norwegian_words.json': 1000, 'Pashto_words.json': 1000, 'Persian_words.json': 1000, 'Polish_words.json': 1000, 'Portuguese_words.json': 1000, 'Punjabi_words.json': 1000, 'Romanian_words.json': 1000, 'Russian_words.json': 1000, 'Samoan_words.json': 1000, 'Serbian_words.json': 1000, 'Sesotho_words.json': 1000, 'Shona_words.json': 1000, 'Sindhi_words.json': 1000, 'Sinhala_words.json': 1000, 'Slovak_words.json': 1000, 'Slovenian_words.json': 1000, 'Somali_words.json': 1000, 'Spanish_words.json': 1000, 'Sundanese_words.json': 1000, 'Swahili_words.json': 1000, 'Swedish_words.json': 1000, 'Tajik_words.json': 1000, 'Tamil_words.json': 1000, 'Telugu_words.json': 1000, 'Thai_words.json': 1000, 'Turkish_words.json': 1000, 'Ukrainian_words.json': 1000, 'Urdu_words.json': 1000, 'Uzbek_words.json': 1000, 'Vietnamese_words.json': 1000, 'Welsh_words.json': 1000, 'Xhosa_words.json': 1000, 'Yiddish_words.json': 1000, 'Yoruba_words.json': 1000, 'Zulu_words.json': 1000}
```
