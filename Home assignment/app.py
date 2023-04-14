from flask import Flask, request, jsonify, render_template
from datetime import datetime
import requests
from bs4 import BeautifulSoup

app = Flask(__name__, template_folder='templates')

def get_numbers_count(numbers, lookback_years):
    start_year = datetime.now().year - lookback_years
    end_year = datetime.now().year

    nums = set(numbers.split(','))
    count = 0
    years = []

    for year in range(start_year, end_year + 1):
        url = f"https://www.euro-jackpot.net/en/results-archive-{year}"
        headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 11; Pixel 2; DuplexWeb-Google/1.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Mobile Safari/537.36"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            for row in soup.find_all('tr')[1:]:
                date = row.find('td').text.strip()
                ball_nums = [int(li.text.strip()) for li in row.find_all('li', class_='ball')]
                draw_nums = set(ball_nums)

                if nums.issubset(draw_nums):
                    count += 1
                    years.append(year)
        else:
            print(f"Error fetching data for year {year}: {response.status_code}")
    
    return {'total_count': count, 'years': years}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        numbers = request.form['numbers']
        lookback_years = int(request.form['lookback_years'])
        result = get_numbers_count(numbers, lookback_years)
        total_count = result['total_count']
        return render_template('result.html', numbers=numbers, lookback_years=lookback_years, total_count=total_count, years=result['years'])
    except ValueError:
        return jsonify({'error': 'Invalid input. Please enter a valid number of years.'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
