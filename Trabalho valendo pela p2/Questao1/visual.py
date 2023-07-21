

class Visualizavel(object):

    max_nivel_visual = 1  

    def visual(self,nivel,*args,**nargs):

        if nivel <= self.max_nivel_visual:
            print(*args, **nargs) 

def visualize(func):

    return func
