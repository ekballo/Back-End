<?php
    class Pessoa{
        //Objeto pessoa

        private $nome = 'Jefferson';
        private $idade = '32';
        private $peso = '113kg';

        public function crescer(){
            $this->comer();
            echo 'estou crescendo';
        }

        private function comer(){
            echo 'estou comendo';
        }

    }

    //Instaciar
    $pessoa = new Pessoa;
    $pessoa = new Pessoa;

    $pessoa->crescer();
?>
