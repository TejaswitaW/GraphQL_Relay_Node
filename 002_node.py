import graphene
from graphene import relay

class Ship(graphene.ObjectType):
    '''A ship in the Star Wars saga'''
    class Meta:
        interfaces = (relay.Node,)
    name = graphene.String(description="The name of the ship")

    @classmethod
    def get_node(cls,info,id):
        return get_ship(id)

    def get_ship(self,args=None):
        return 3

ship_one=Ship()
print(ship_one.get_node(info="my",id=1))