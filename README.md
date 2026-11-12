# git-kurss
Programmatūras ieviešanas un uzturēšanas dzīves cikls un procesu automatizācija
Pirmā izmaiņa

## Kalkulators

Fails `practice.py` satur kalkulatora galveno funkciju. Tā ļauj izvēlēties saskaitīšanu vai reizināšanu, ievadīt veselus skaitļus un atkārtot aprēķinus. Atbalsta funkcijas (`add_numbers`, `multiply_numbers`, `read_integer`, `select_operation` un `ask_to_repeat`) atrodas failā `utils.py`. Nederīgas izvēles vai ievades gadījumā programma pieprasa ievadīt vērtību atkārtoti.

Lai palaistu kalkulatoru no projekta mapes:

```bash
python practice.py
```

Testi atrodas failā `test_practice.py` un pārbauda matemātiskās funkcijas, nederīgas ievades apstrādi, darbības izvēli un aprēķinu atkārtošanu. Lai palaistu testus:

```bash
python -m unittest -v test_practice
```
