Ustvarite mapo "data" in vanjo prenesite datoteke iz:
- https://drive.google.com/open?id=1RQ6hD0N9U8aZYqcBV_-jGJokTyFctr7L

Ustvarite mapo "wordvecs" in vanjo prenesite:
- http://nlp.stanford.edu/data/glove.42B.300d.zip
- http://nlp.stanford.edu/data/glove.840B.300d.zip

Prenesite vse modele:
- https://drive.google.com/open?id=1ILSyozgtRD5gWHM3uNRvLVwseD1syxuB
Mape z modeli tudi že vsebujejo vse zgenerirane rezultate z izjemo grafov.

Za dodatne eksperimente ustvarite mapo "lib" in vanjo prenesite celotno CoreNLP orodje omenjeno v poročilu.
```sh
java -mx4g -cp "lib/*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000
```

Koda trenutno deluje samo na specifičnih modelih. Za zagon posameznih uporabite ukaze:

Temeljni model
```sh
 python rc/main.py --pretrained rc_models_20
```

Samo zgodovina
```sh
python rc/main.py --pretrained rc_models_modified_20
```

Zgodovina + trenutno vprašanje
```sh
python rc/main.py --pretrained rc_models_modified_full_noA_20
```
  

Zgodovina + trenutno vprašanje + trenutni odgovor
```sh
 python rc/main.py --pretrained rc_models_modified_full_20
```


Grafe lahko generirate z:
```sh
 python plot_metrics.py
```




