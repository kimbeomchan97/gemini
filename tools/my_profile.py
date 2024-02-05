import google.ai.generativelanguage as glm

_my_profile = glm.Tool(
  function_declarations=[
    glm.FunctionDeclaration(
      name='beomchankim',
      description="showing user's name",
      parameters=glm.Schema(
        type=glm.Type.OBJECT,
        required=[]
      )
    )
  ]
)