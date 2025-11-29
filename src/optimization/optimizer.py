class Optimizer:
    def optimize(self, instructions):
        
        changed = True
        current_ir = instructions
        while changed:
            changed = False
            
            new_ir, folded = self.constant_propagation(current_ir)
            if folded:
                changed = True
                current_ir = new_ir
            
            new_ir, eliminated = self.dead_code_elimination(current_ir)
            if eliminated:
                changed = True
                current_ir = new_ir
                
        return current_ir

    def constant_propagation(self, instructions):
        
        constants = {}
        new_instructions = []
        changed = False

        for op, arg1, arg2, result in instructions:
            
            if arg1 in constants:
                arg1 = constants[arg1]
                changed = True
            if arg2 in constants:
                arg2 = constants[arg2]
                changed = True

            
            if self.is_number(arg1) and (arg2 is None or self.is_number(arg2)):
                if op == 'ASSIGN':
                    constants[result] = arg1
                    new_instructions.append(('ASSIGN', arg1, None, result))
                elif op in ('ADD', 'SUB', 'MUL', 'DIV'):
                    val1 = int(arg1)
                    val2 = int(arg2)
                    res = 0
                    if op == 'ADD': res = val1 + val2
                    elif op == 'SUB': res = val1 - val2
                    elif op == 'MUL': res = val1 * val2
                    elif op == 'DIV': res = val1 // val2 
                    
                    constants[result] = str(res)
                    
                    new_instructions.append(('ASSIGN', str(res), None, result))
                    changed = True
                else:
                    new_instructions.append((op, arg1, arg2, result))
            else:
                
                
                
                
                if result in constants and op != 'ASSIGN': 
                    
                    del constants[result]
                
                
                if op == 'ASSIGN' and not self.is_number(arg1):
                     if result in constants: del constants[result]

                new_instructions.append((op, arg1, arg2, result))
        
        return new_instructions, changed

    def dead_code_elimination(self, instructions):
        
        used_vars = set()
        for op, arg1, arg2, result in instructions:
            if arg1: used_vars.add(arg1)
            if arg2: used_vars.add(arg2)
            
        new_instructions = []
        changed = False
        
        for instr in instructions:
            op, arg1, arg2, result = instr
            
            if result.startswith('t') and result not in used_vars:
                changed = True
                continue
            new_instructions.append(instr)
            
        return new_instructions, changed

    def is_number(self, s):
        if s is None: return False
        try:
            int(s)
            return True
        except ValueError:
            return False
