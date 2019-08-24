# Whois Microservice "Nadavê"

Using this shit to implement microservices tests on containers.

This is a 5 minute implementation. Don't use this like reference for nothing. 

### How to create setup with docker

```sh
docker run -it -p 5000:5000 msfidelis/faker:v1

```

## How to use 

### Random Person Generator

```sh
curl  http://127.0.0.1:5000/faker -i
```

```
{
  "address": "Rua João Duarte, 547\nNova Cintra\n81069759 Vieira / PR",
  "blood_group": "O+",
  "company": "da Rosa",
  "cpf": "793.412.068-04",
  "job": "Ginecologista",
  "license_plate": "QNT-5257",
  "name": "Sr. Antônio das Neves",
  "residence": "Loteamento Carlos Eduardo Jesus, 9\nNossa Senhora Da Conceição\n46386-332 Silva / RS",
  "rg": "051328641",
  "sex": "M"
}
```

### Male Person Generator

```sh
curl  http://127.0.0.1:5000/faker/male -i
```

```
{
  "address": "Quadra de Nascimento, 69\nVila Real 2ª Seção\n48954-437 Moraes Verde / MG",
  "blood_group": "AB-",
  "company": "Oliveira",
  "cpf": "582.746.309-47",
  "job": "Turismólogo",
  "license_plate": "SKN-8908",
  "name": "Pedro Miguel Silveira",
  "residence": "Chácara Lorena da Rocha, 31\nIndaiá\n80789869 da Paz da Praia / MA",
  "rg": "576238405",
  "sex": "M"
}
```


### Female Person Generator

```sh
curl  http://127.0.0.1:5000/faker/female -i
```

```
{
  "address": "Distrito Luiz Fernando Martins, 23\nVila Rica\n02374-202 Souza do Galho / AL",
  "blood_group": "B-",
  "company": "da Luz",
  "cpf": "458.739.612-55",
  "job": "Escriturário",
  "license_plate": "LXT-0561",
  "name": "Emanuelly Silva",
  "residence": "Parque Santos, 85\nConjunto Santa Maria\n35563-548 Alves / GO",
  "rg": "538746026",
  "sex": "F"
}
```