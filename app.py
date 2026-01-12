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
        'address': 'Opp. Hotel Red Diamond, Bram Baba Road, Bilaspur, Chhattisgarh, India',
        'contacts': ['+91 95750 15001', '+91 96176 05544']
    },
    {
        'name': 'Hotel Red Diamond',
        'sector': 'Hospitality',
        'description': 'Hotel Red Diamond is a premium hospitality destination offering comfort, elegance, and warm service. Designed for both business and leisure travelers, the hotel delivers a refined stay experience with modern amenities and a welcoming atmosphere.',
        'logo': 'red_diamond_hotel_logo.png',
        'address': 'Old Power House, Road, Torwa, Bilaspur, Chhattisgarh 495004',
        'contacts': ['+91 98279 00051']
    },
    {
        'name': 'Red Diamond Sports Center',
        'sector': 'Sports and Recreation',
        'description': 'Red Diamond Sports Center is a dedicated space for fitness, sports, and active living. With well-equipped facilities and a focus on overall well-being, it encourages a healthy lifestyle for individuals, families, and sports enthusiasts.',
        'logo': 'red_diamond_sport_center_logo.jpg',
        'address': 'Opposite Hotel Red Diamond, Old Power House, Road, Torwa, Bilaspur, Chhattisgarh 495004',
        'contacts': ['+91 98279 00051']
    },
    {
        'name': 'Rising Star Turf',
        'sector': 'Sports Infrastructure',
        'description': 'Rising Star Turf is a professional cricket turf developed for players of all levels. Built to support training, practice matches, and competitive play, it provides a high-quality sporting environment for cricket lovers and aspiring athletes.',
        'logo': 'rising_star.jpg',
        'address': 'Gurunanak Chowk, near Life Care Hospital, Torwa, Bilaspur, Chhattisgarh 495004',
        'contacts': ['+91 98279 00051']
    },
    {
        'name': 'Chocolate Kids School',
        'sector': 'Education',
        'description': 'Chocolate Kids School is an early education institution focused on nurturing young minds in a safe and joyful environment. With a balance of learning and play, the school emphasizes creativity, values, and strong foundational development.',
        'logo': 'school_img.jpg',
        'address': 'Jagmal Chowk, opposite Yamaha Showroom, Torwa, Bilaspur, Chhattisgarh 495004',
        'contacts': ['+91 98279 00051']
    },
    {
        'name': 'UB Group of Companies',
        'sector': 'Conglomerate',
        'description': 'UB Group of Companies is a diversified business conglomerate with interests in real estate, hospitality, sports, and education. With a commitment to quality and innovation, we aim to bring dreams together under one roof.',
        'logo': 'ubgrouplogo.jpeg',
        'address': 'Opp. Hotel Red Diamond, Bram Baba Road, Bilaspur, Chhattisgarh, India',
        'contacts': ['+91 95750 15001', '+91 96176 05544', '+91 98279 00051']
    }
]

# Leadership data
leadership = [
    {'name': 'Ashish Ubhrani', 'position': 'MD', 'business': 'UB World', 'photo': 'ashishsir.jpeg', 'bio': 'With a strategic vision for modern living, Ashish Ubhrani leads UB World in creating residential spaces that blend comfort, quality, and community.', 'css_class': 'ashish-ubhrani'},
    {'name': 'Rahul Ubhrani', 'position': 'MD', 'business': 'UB World', 'photo': 'rahul_sir_logo.jpg', 'bio': 'Rahul Ubhrani is dedicated to executing the vision of UB World, focusing on delivering homes that offer a perfect balance of lifestyle and long-term value.', 'css_class': 'rahul-ubhrani'},
    {'name': 'Abhinav Ubhrani', 'position': 'MD', 'business': 'Hotel Red Diamond', 'photo': 'abhinav_sir.jpg', 'bio': 'Abhinav Ubhrani oversees Hotel Red Diamond, ensuring a premium hospitality experience that combines elegance, comfort, and exceptional service for all guests.', 'css_class': 'abhinav-ubhrani'},
    {'name': 'Karan Ubhrani', 'position': 'MD', 'business': 'Hotel Red Diamond', 'photo': 'karan.jpg', 'bio': 'Karan Ubhrani plays a key role in managing Hotel Red Diamond, focusing on operational excellence and maintaining a welcoming atmosphere for travelers.', 'css_class': 'karan-ubhrani'},
    {'name': 'Manish Ubhrani', 'position': 'MD', 'business': 'Red Diamond Sports Center', 'photo': 'mahish.jpg', 'bio': 'Manish Ubhrani leads the Red Diamond Sports Center, promoting a culture of fitness and well-being by providing state-of-the-art facilities for sports enthusiasts.', 'css_class': 'manish-ubhrani'},
    {'name': 'Mohit Ubhrani', 'position': 'MD', 'business': 'Rising Star Turf', 'photo': None, 'bio': 'Mohit Ubhrani is the driving force behind Rising Star Turf, a professional-grade cricket facility designed to nurture talent and support the local sporting community.', 'css_class': 'mohit-ubhrani'},
    {'name': 'Saina Ubhrani', 'position': 'MD', 'business': 'Chocolate Kids School', 'photo': 'saina.jpg', 'bio': 'Saina Ubhrani heads Chocolate Kids School, where she is committed to fostering a joyful and nurturing learning environment for early education.', 'css_class': 'saina-ubhrani'}
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
