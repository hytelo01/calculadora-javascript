/* POO - JavaScript */

/*Criando a classe 
1 - Digita-se a palavra reservada class;
2 - Dá-se o nomde à classe. Geralemente, o nome coemaç com a primeira letra maiúscula;
3 - OS ATRIBUTOS E METODOS SÃO ABREVIADOS ENTRE CHAVES;
4 - É criado o método construtor usando a palavra construtor, onde são criados os atributos e 'transformados' em variáveis;
5 - Os métodos são funções como outra qualquer, porém é feita a referencia ou não aos atributos criados. Quando for usados os atributos, é necessario
usar a palavra 'this';
6 - Para criar um novo objeto, é necessario dar uma variavel ( var ou let ), um nome à variavel e igualar a palavra 'new'
mais a classe criada. 
*/

class carro{
    constructor(marca, categoria, modelo, cor){

        this.marca = marca
        this.categoria =  categoria
        this.modelo = modelo
        this.cor = cor
    }

    acelerar(){
        return "${this.modelo} acelera de 0 a 100 em 10 segundos"
    }
    carregar(){
        return "carrega até 200kg "
    }

}

let carro1 = new carro("Ford", "hatch", "For KA", vermelho)
console.log(carro1)
let c1 = carro1.acelerar()
console.log(c1)