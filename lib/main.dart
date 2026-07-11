import 'package:flutter/material.dart';

void main() {
  runApp(UnitConverterApp());
}

class UnitConverterApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Unit Converter',
      theme: ThemeData.dark(),
      home: ConverterScreen(),
    );
  }
}

class ConverterScreen extends StatefulWidget {
  @override
  _ConverterScreenState createState() => _ConverterScreenState();
}

class _ConverterScreenState extends State<ConverterScreen> {
  TextEditingController inputController = TextEditingController();
  String fromUnit = 'Meters';
  String toUnit = 'Kilometers';
  String result = '';
  
  List<String> units = ['Meters', 'Kilometers', 'Grams', 'Kilograms'];

  void convert() {
    double val = double.tryParse(inputController.text) ?? 0;
    double res = val;

    // Length
    if (fromUnit == 'Meters' && toUnit == 'Kilometers') res = val / 1000;
    if (fromUnit == 'Kilometers' && toUnit == 'Meters') res = val * 1000;
    
    // Weight
    if (fromUnit == 'Grams' && toUnit == 'Kilograms') res = val / 1000;
    if (fromUnit == 'Kilograms' && toUnit == 'Grams') res = val * 1000;
    
    setState(() {
      result = res.toString();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Unit Converter')),
      body: Padding(
        padding: EdgeInsets.all(20),
        child: Column(
          children: [
            TextField(
              controller: inputController,
              keyboardType: TextInputType.number,
              decoration: InputDecoration(
                labelText: 'Weka namba hapa',
                border: OutlineInputBorder(),
              ),
              style: TextStyle(fontSize: 24),
            ),
            SizedBox(height: 20),
            DropdownButtonFormField(
              value: fromUnit,
              items: units.map((u) => DropdownMenuItem(value: u, child: Text(u))).toList(),
              onChanged: (v) => setState(() => fromUnit = v!),
              decoration: InputDecoration(border: OutlineInputBorder()),
            ),
            SizedBox(height: 20),
            DropdownButtonFormField(
              value: toUnit,
              items: units.map((u) => DropdownMenuItem(value: u, child: Text(u))).toList(),
              onChanged: (v) => setState(() => toUnit = v!),
              decoration: InputDecoration(border: OutlineInputBorder()),
            ),
            SizedBox(height: 30),
            ElevatedButton(
              onPressed: convert,
              child: Text('Convert', style: TextStyle(fontSize: 24)),
              style: ElevatedButton.styleFrom(
                minimumSize: Size(double.infinity, 60),
                backgroundColor: Colors.blue,
              ),
            ),
            SizedBox(height: 30),
            Text('Jibu: $result', style: TextStyle(fontSize: 32, color: Colors.green)),
          ],
        ),
      ),
    );
  }
}
