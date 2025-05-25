# Todo Application

A feature-rich task management application built with Python and PyQt5.

## Features

- 📋 Task Management
  - Create, edit, and delete tasks
  - Set due dates and priorities
  - Add descriptions and attachments
  - Create subtasks
  - Mark tasks as complete

- 📁 Category Organization
  - Create custom categories
  - Filter tasks by category
  - Easy category management

- 📅 Calendar Integration
  - View tasks by date
  - Calendar-based task planning
  - Date-based filtering

- 📊 Statistics
  - Track task completion rates
  - View productivity metrics
  - Task distribution by category

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/todo.git
cd todo
```

2. Create and activate a virtual environment (recommended):
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/MacOS
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python main.py
```

## Dependencies

- Python 3.8+
- PyQt5
- SQLAlchemy
- Python-dateutil

## Features Details

### Task Management
- Create tasks with titles and descriptions
- Set due dates and priority levels
- Add attachments to tasks
- Create subtasks for better organization
- Mark tasks as complete

### Categories
- Create custom categories for tasks
- Filter tasks by category
- Edit and delete categories
- Category-based task organization

### Calendar View
- Interactive calendar interface
- View tasks by date
- Filter tasks based on due dates
- Date-based task planning

### Statistics
- View task completion rates
- Track productivity over time
- Category-based task distribution
- Progress monitoring

## Development

### Adding New Features

1. Create necessary model classes in `models/`
2. Implement business logic in `services/`
3. Create UI components in `gui/`
4. Update main application to integrate new features

### Database Schema Updates

1. Modify relevant model classes
2. Handle migrations if needed
3. Update corresponding services

### UI Modifications

1. Create or modify widgets in `gui/widgets/`
2. Update dialogs in `gui/dialogs/`
3. Integrate changes with main window

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

- **Ngou1200** - *Initial work*

## Support

For support, please open an issue in the GitHub repository.

## Acknowledgments

- PyQt5 for the GUI framework
- SQLAlchemy for database management
- All contributors who have helped with the project
