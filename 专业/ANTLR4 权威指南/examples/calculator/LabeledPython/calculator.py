from antlr4 import *  
from LabeledExprVisitor import LabeledExprVisitor  
from LabeledExprParser import LabeledExprParser  
from LabeledExprLexer import LabeledExprLexer  
  
class LabeledExprulatorVisitor(LabeledExprVisitor):  

    def visitAssign(self, ctx:LabeledExprParser.AssignContext):
        id = ctx.ID().getText()
        value = self.visit(ctx.expr())
        return value

    def visitPrintExpr(self, ctx:LabeledExprParser.PrintExprContext):  
        value = self.visit(ctx.expr())
        print(value)
        return 0  

    def visitInt(self, ctx:LabeledExprParser.IntContext ):
        return int(ctx.INT().getText())
    
  
    def visitId(self, ctx:LabeledExprParser.IdContext):
        id = ctx.ID().getText()
        return 0

    def visitMuldiv(self, ctx:LabeledExprParser.MuldivContext):
        left = self.visit(ctx.expr(0))  
        right = self.visit(ctx.expr(1))
        if ctx.getChild(1).getText() == '*':
            return left * right  
        else:  
            return left / right  
  
    def visitAddSub(self, ctx:LabeledExprParser.AddSubContext):
        left = self.visit(ctx.expr(0))  
        right = self.visit(ctx.expr(1))  
        if ctx.getChild(1).getText() == '+':
            return left + right  
        else:  
            return left - right  
    
    def visitParens(self, ctx:LabeledExprParser.ParensContext):
        return self.visit(ctx.expr())

def evaluate(expression):  
    input_stream = InputStream(expression)  
    lexer = LabeledExprLexer(input_stream)  
    stream = CommonTokenStream(lexer)  
    parser = LabeledExprParser(stream)  
    tree = parser.expr()  
    visitor = LabeledExprulatorVisitor()  
    return visitor.visit(tree)  
  
if __name__ == "__main__":  
    expression = input("Enter an expression: ")  
    print(evaluate(expression))