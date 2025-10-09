# batalha.py - Sistema de Batalha RPG com POO
from abc import ABC, abstractmethod
import random

class Personagem(ABC):
    """Classe abstrata base para todos os personagens"""
    
    def __init__(self, nome, vida, ataque_base):
        self.nome = nome  # público
        self._vida = vida  # protegido
        self._ataque_base = ataque_base  # protegido
    
    # ENCAPSULAMENTO - Controle seguro da vida
    def receber_dano(self, dano):
        """Recebe dano, garantindo que a vida nunca fique negativa"""
        if dano > 0:
            self._vida = max(0, self._vida - dano)
            print(f" {self.nome} recebeu {dano} de dano!")
    
    def esta_vivo(self):
        """Verifica se o personagem está vivo"""
        return self._vida > 0
    
    def get_vida(self):
        """Getter para vida (encapsulamento)"""
        return self._vida
    
    @abstractmethod
    def atacar(self, alvo):
        """Método abstrato - deve ser implementado pelas subclasses"""
        pass


class Guerreiro(Personagem):
    """Classe para personagens do tipo Guerreiro"""
    
    def __init__(self, nome, vida=100, ataque_base=15):
        super().__init__(nome, vida, ataque_base)
        self.__furia = 0  # privado
    
    # ENCAPSULAMENTO - Controle da fúria
    def __ganhar_furia(self, quantidade):
        """Método privado para gerenciar fúria"""
        self.__furia = min(100, self.__furia + quantidade)
    
    def get_furia(self):
        """Getter para fúria"""
        return self.__furia
    
    # POLIMORFISMO - Implementação específica
    def atacar(self, alvo):
        """Ataque básico do guerreiro"""
        dano = self._ataque_base + random.randint(1, 5)
        alvo.receber_dano(dano)
        self.__ganhar_furia(10)  # Ganha fúria ao atacar
        print(f" {self.nome} ataca com espada! +10 de fúria")
        return dano
    
    def ataque_especial(self, alvo):
        """Ataque especial que consome fúria"""
        if self.__furia >= 30:
            dano = self._ataque_base + 20 + random.randint(5, 10)
            alvo.receber_dano(dano)
            self.__furia -= 30  # Consome fúria
            print(f" {self.nome} usa ATAQUE FURIOSO! -30 de fúria")
            return dano
        else:
            print(f" {self.nome} não tem fúria suficiente para ataque especial!")
            return 0


class Mago(Personagem):
    """Classe para personagens do tipo Mago"""
    
    def __init__(self, nome, vida=80, ataque_base=10):
        super().__init__(nome, vida, ataque_base)
        self.__mana = 100  # privado
    
    # ENCAPSULAMENTO - Controle da mana
    def __consumir_mana(self, quantidade):
        """Método privado para consumir mana"""
        if self.__mana >= quantidade:
            self.__mana -= quantidade
            return True
        return False
    
    def get_mana(self):
        """Getter para mana"""
        return self.__mana
    
    def recuperar_mana(self):
        """Recupera mana a cada turno"""
        self.__mana = min(100, self.__mana + 5)
    
    # POLIMORFISMO - Implementação específica
    def atacar(self, alvo):
        """Ataque mágico do mago"""
        if self.__consumir_mana(15):
            dano = self._ataque_base + random.randint(10, 20)
            alvo.receber_dano(dano)
            print(f" {self.nome} lança ESPIRITOS DAS SOMBRAS! -15 de mana")
            return dano
        else:
            print(f" {self.nome} não tem mana suficiente! Recuperando...")
            self.recuperar_mana()
            return 0


# SIMULAÇÃO DA BATALHA
if __name__ == "__main__":
    print("=" * 50)
    print("          BATALHA RPG - GUERREIRO vs MAGO")
    print("=" * 50)
    
    # Criando os personagens
    guerreiro = Guerreiro("Dark Lord", vida=120, ataque_base=18)
    mago = Mago("Wizard", vida=90, ataque_base=15)
    
    turno = 1
    
    # Loop principal da batalha
    while guerreiro.esta_vivo() and mago.esta_vivo():
        print(f"\n TURNO {turno}")
        print("-" * 30)
        
        # Status dos personagens
        print(f" {guerreiro.nome}: Vida {guerreiro.get_vida()} | Fúria {guerreiro.get_furia()}")
        print(f" {mago.nome}: Vida {mago.get_vida()} | Mana {mago.get_mana()}")
        print("-" * 30)
        
        # Turno do Guerreiro
        if guerreiro.esta_vivo():
            if guerreiro.get_furia() >= 30 and random.random() > 0.6:  # 40% chance de especial
                guerreiro.ataque_especial(mago)
            else:
                guerreiro.atacar(mago)
        
        # Turno do Mago
        if mago.esta_vivo():
            mago.atacar(guerreiro)
            mago.recuperar_mana()  # Recupera mana a cada turno
        
        turno += 1
    
    # Resultado final
    print("\n" + "=" * 50)
    print("              FIM DA BATALHA!")
    print("=" * 50)
    
    if guerreiro.esta_vivo():
        print(f" VITÓRIA DO {guerreiro.nome}!")
        print(f"Vida restante: {guerreiro.get_vida()}")
    elif mago.esta_vivo():
        print(f" VITÓRIA DO {mago.nome}!")
        print(f"Vida restante: {mago.get_vida()}")
    else:
        print(" EMPATE! Ambos foram derrotados.")