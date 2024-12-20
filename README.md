# travelectable
The Travel Site Made with Generative AI Love 

## Useful links as we build our site
### Amadeus
* [Amadeus Python API](https://github.com/amadeus4dev/amadeus-python)
* [Amadeus Django App](https://github.com/amadeus4dev/amadeus-hotel-booking-django/blob/master/amadeus_demo_api/demo/views.py)
* [Self-Service API docs for Amadeus](https://developers.amadeus.com/self-service/apis-docs)

## ChatGPT tells me this is our color scheme ##
Certainly! Here are some colors that accompany blue well, along with suggestions on where to use them on your travel site:

1. **Blue (#0074D9)**: Use this as the primary color for your site's header, navigation menu, and prominent call-to-action buttons. Blue conveys trust, reliability, and a sense of calm, making it ideal for establishing a positive first impression.

2. **White (#FFFFFF)**: Utilize white as the background color for your site to create a clean and spacious layout. It helps content stand out and ensures readability.

3. **Light Gray (#CCCCCC)**: Use light gray for secondary elements such as borders, dividers, and background accents. It adds depth to your design without overwhelming the blue and white color scheme.

4. **Teal (#39CCCC)**: Teal can be used sparingly to add visual interest and contrast to specific sections or elements, such as hover effects, icons, or selected buttons.

5. **Navy Blue (#001f3f)**: Incorporate navy blue for text elements, such as headlines, paragraphs, and links. It provides a darker shade of blue that still complements the primary blue hue while enhancing readability.

6. **Sky Blue (#87CEEB)**: Use sky blue for background accents or highlights, particularly in sections where you want to evoke a sense of openness or freedom, such as images of clear skies or open landscapes.

7. **Gold (#FFD700)**: Add touches of gold for special elements like badges, awards, or premium offerings. Gold contrasts beautifully with blue and adds a touch of luxury or exclusivity to your site.

8. **Slate Gray (#2c3e50)**: Consider using slate gray for footer sections or other areas where you want to maintain a professional and grounded appearance. It provides a subtle contrast to the primary blue color while maintaining a cohesive look.

By incorporating these colors strategically throughout your website, you can create a visually appealing and cohesive design that reflects the trustworthiness, reliability, and serenity associated with blue, while also enhancing readability and user experience.

## Mock Data Creation Notes
### For locations
1. Execute the query for metro areas listed at the top of `parse_us_cities.py`.
2. If necessary, make adjustments to the code to parse the result of that query to populate
the source US cities list.
3. Run `parse_us_cities.py` to generate the `us_cities.txt` file with metro statistics.
4. Run `generate_lat_long_us_cities.py` to update the `us_cities.txt`

## Initial airport query
For the airports LAX and ORD, generate 4 flight plans in each direction and list whether or not they're non-stop.  If they're multiple stop, list the airports.

## Refined airport query
For the airports LAX and ORD generate 16 flight plans:

8 for LAX to ORD
8 for ORD to LAX

Structure the output as:
Origin | Destination | Airline | (Number of stops (and layover airport(s)))|Departure Time| Arrival Time| Total price in USD

Use 24-hour time for departure and arrival.

You do not need to provide city names, only airport codes.  

Do not provide any preamble, summary, or disclaimer or any statements like "Here are the 16 flight plans".  Only provide the information requested in the format specified.  The information does not need to be accurate but needs to appear accurate.

### Number of queries for the total number of airports
(n-1)*(n-2)/2

Each query consumes approximately 600 tokens

The total number of tokens will be somewhere around 3M.

[Airport distances](https://airport4.docs.apiary.io/#reference/0/distance-between-airports/get-distance?console=1)

[A less restrictive airport distance API](https://airportgap.com/docs)

[A download of airports and their locations](https://openflights.org/data.php)

[Using this as the seat map guide.](https://www.seatguru.com/airlines/United_Airlines/United_Airlines_Boeing_777-200_6.php)

