import requests

if __name__ == '__main__':

    try:

        # GET request - ONE
        responseOne = requests.get('https://jsonplaceholder.typicode.com/todos/1')
        print(responseOne.text)

        # GET request - ALL
        responseTwo = requests.get('https://jsonplaceholder.typicode.com/todos')
        print(responseTwo.text)

        # DELETE request - ONE
        responseThree = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
        print(responseThree.text)

        # PUT request - ONE
        responseFour = requests.put('https://jsonplaceholder.typicode.com/posts/1', data = {"title":"Updated!"})
        print(responseFour.text)

        # POST request - ONE
        responseFive = requests.post('https://jsonplaceholder.typicode.com/posts', data = {
            "userId": -1,
             "id": -1,
            "title": "Posted"
        })
        print(responseFive.text)

    except Exception as ex:

        print('Exception! ' + str(ex))