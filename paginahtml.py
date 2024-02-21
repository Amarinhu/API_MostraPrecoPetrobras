pghtml = """
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Basic HTML Page</title>
    </head>
    <body style="font-family: Arial, sans-serif; text-align: center; margin: 50px;">

        <h1>Mercury API</h1>
        <p style="margin-bottom: 20px;">Welcome to my first API</p>
        <p style="margin-bottom: 10px;">By: Mercury Raven</p>

        <a href='/api/mostra-preco'>
        <button style="padding: 10px 20px; font-size: 16px; background-color: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer;"
                onmouseover="this.style.backgroundColor='#45a049'" 
                onmouseout="this.style.backgroundColor='#4CAF50'" ">
            Gerar Preço!
        </button>
        </a>

        <p style="margin-bottom: 14px;">This API captures the average price of gasoline in DF (Brazil) from the Petrobras website.</p>

    </body>
    </html>
"""