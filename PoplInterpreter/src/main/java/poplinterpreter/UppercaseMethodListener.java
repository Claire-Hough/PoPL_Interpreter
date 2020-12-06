/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package poplinterpreter;


import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import org.antlr.v4.runtime.tree.TerminalNode;

/**
 *
 * @author Claire
 */
public class UppercaseMethodListener extends Java8BaseListener {

    private List<String> errors = new ArrayList<String>();

    @Override
    public void enterMethodDeclarator(Java8Parser.MethodDeclaratorContext ctx) {
        TerminalNode node = ctx.Identifier();
        String methodName = node.getText();

        if (Character.isUpperCase(methodName.charAt(0))){
            errors.add(String.format("Method %s is uppercased!", methodName));
        }
    }

    public List<String> getErrors(){
        return Collections.unmodifiableList(errors);
    }
}