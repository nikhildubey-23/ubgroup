from flask import Flask, render_template

app = Flask(__name__)

# Group information
group_info = {
    'name': 'UB GROUP',
    'tagline': 'BRINGING DREAMS TOGETHER UNDER ONE ROOF',
    'overview': '"UB Group is a diverse organization bringing together multiple ventures under one umbrella. From UB World\'s residential spaces to hospitality at Hotel Red Diamond, and educational initiatives like Chocolate Kidz School, we aim to create a comprehensive community experience. Each project reflects our commitment to quality, comfort, and innovation, all under the UB Group name."',
    'about_us': '"At UB Group, we believe in creating a holistic community experience by uniting a variety of ventures under one roof. Our portfolio spans residential living with UB World, top-tier hospitality at Hotel Red Diamond, quality education through Chocolate Kids School, and vibrant lifestyle amenities like the Red Diamond Sports Center. Each of our projects reflects our commitment to quality, comfort, and innovation, all designed to enrich the lives of our customers and community. We take pride in being a trusted name that brings dreams together under one roof."'
}

# Businesses data
businesses = [
    {
        'name': 'UB World',
        'sector': 'Real Estate',
        'description': 'UB World is a modern real estate venture focused on creating thoughtfully designed residential spaces. Built around comfort, quality, and community living, UB World aims to offer homes that balance lifestyle, convenience, and long-term value.',
        'logo': 'ubworld.jpeg',
        'address': None,
        'contacts': ['ASHISH UBHRANI - 9617605544', 'RAHUL UBHRANI - 9827900051']
    },
    {
        'name': 'Hotel Red Diamond',
        'sector': 'Hospitality',
        'description': 'Hotel Red Diamond is a premium hospitality destination offering comfort, elegance, and warm service. Designed for both business and leisure travelers, the hotel delivers a refined stay experience with modern amenities and a welcoming atmosphere.',
        'logo': 'red_diamond_hotel_logo.png',
        'address': 'Old Power House, Road, Torwa, Bilaspur, Chhattisgarh 495004',
        'contacts': ['ABHINAV UBHRANI - 9111911145', 'KARAN UBHRANI - 9752646999']
    },
    {
        'name': 'Red Diamond Sports Center',
        'sector': 'Sports and Recreation',
        'description': 'Red Diamond Sports Center is a dedicated space for fitness, sports, and active living. With well-equipped facilities and a focus on overall well-being, it encourages a healthy lifestyle for individuals, families, and sports enthusiasts.',
        'logo': 'red_diamond_sport_center_logo.jpg',
        'address': 'Opposite Hotel Red Diamond, Old Power House, Road, Torwa, Bilaspur, Chhattisgarh 495004',
        'contacts': ['MANISH UBHRANI - 9977736888']
    },
    {
        'name': 'Rising Star Turf',
        'sector': 'Sports Infrastructure',
        'description': 'Rising Star Turf is a professional cricket turf developed for players of all levels. Built to support training, practice matches, and competitive play, it provides a high-quality sporting environment for cricket lovers and aspiring athletes.',
        'logo': 'rising_star.jpg',
        'address': 'Gurunanak Chowk, near Life Care Hospital, Torwa, Bilaspur, Chhattisgarh 495004',
        'contacts': ['MOHIT UBHRANI - 7898628881']
    },
    {
        'name': 'Chocolate Kids School',
        'sector': 'Education',
        'description': 'Chocolate Kids School is an early education institution focused on nurturing young minds in a safe and joyful environment. With a balance of learning and play, the school emphasizes creativity, values, and strong foundational development.',
        'logo': 'school_img.jpg',
        'address': 'Jagmal Chowk, opposite Yamaha Showroom, Torwa, Bilaspur, Chhattisgarh 495004',
        'contacts': ['SAINA UBHRANI - 8719995554']
    }
]

# Leadership data
leadership = [
    {'name': 'ASHISH UBHRANI', 'position': 'MD', 'business': 'UB World', 'photo': 'ashishsir.jpeg'},
    {'name': 'RAHUL UBHRANI', 'position': 'MD', 'business': 'UB World', 'photo': 'rahul_sir_logo.jpg'},
    {'name': 'ABHINAV UBHRANI', 'position': 'MD', 'business': 'Hotel Red Diamond', 'photo': 'abhinav_sir.jpg'},
    {'name': 'KARAN UBHRANI', 'position': 'MD', 'business': 'Hotel Red Diamond', 'photo': 'karan.jpg'},
    {'name': 'MANISH UBHRANI', 'position': 'MD', 'business': 'Red Diamond Sports Center', 'photo': 'mahish.jpg'},
    {'name': 'MOHIT UBHRANI', 'position': 'MD', 'business': 'Rising Star Turf', 'photo': None},
    {'name': 'SAINA UBHRANI', 'position': 'MD', 'business': 'Chocolate Kids School', 'photo': None}
]

@app.route('/')
def home():
    return render_template('home.html', group_info=group_info, businesses=businesses, leadership=leadership)

@app.route('/about')
def about():
    return render_template('about.html', group_info=group_info)

@app.route('/businesses')
def businesses_page():
    return render_template('businesses.html', group_info=group_info, businesses=businesses)

@app.route('/leadership')
def leadership_page():
    return render_template('leadership.html', group_info=group_info, leadership=leadership)

@app.route('/contact')
def contact():
    return render_template('contact.html', group_info=group_info, businesses=businesses)

if __name__ == '__main__':
    app.run(debug=True)
